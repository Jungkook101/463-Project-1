import csv
from typing import List, Tuple
from datetime import datetime

class StockAnalysisSystem:
    def __init__(self, file_path: str):
        """
        Initialize the system with a file path to the financial data.
        """
        self.file_path = file_path
        self.data = self.load_data_from_file()

    def load_data_from_file(self) -> List[Tuple[datetime, float]]:
        """
        Load data from the CSV file.
        Expects a header row and date in the first column, closing price in the fifth column.
        """
        data = []
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                try:
                    date = datetime.strptime(row[0], "%Y-%m-%d")
                    close_price = float(row[4])
                    data.append((date, close_price))
                except (ValueError, IndexError) as e:
                    print(f"Error processing row {row}: {e}")
                    continue

        if not data:
            raise ValueError("No valid data could be extracted from the file. Please check the file format.")

        return data

    def merge_sort(self, arr: List[Tuple[datetime, float]]) -> List[Tuple[datetime, float]]:
        """
        Merge sort implementation for sorting financial data by closing price.
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left: List[Tuple[datetime, float]], right: List[Tuple[datetime, float]]) -> List[Tuple[datetime, float]]:
        """
        Merge two sorted arrays based on closing price.
        """
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def max_subarray(self, arr: List[float]) -> Tuple[int, int, float]:
        """
        Divide-and-conquer implementation of Kadane's algorithm for maximum subarray.
        Returns (start_index, end_index, max_sum).
        """
        def max_crossing_subarray(arr: List[float], low: int, mid: int, high: int) -> Tuple[int, int, float]:
            left_sum = float('-inf')
            sum = 0
            max_left = mid
            for i in range(mid, low - 1, -1):
                sum += arr[i]
                if sum > left_sum:
                    left_sum = sum
                    max_left = i

            right_sum = float('-inf')
            sum = 0
            max_right = mid + 1
            for i in range(mid + 1, high + 1):
                sum += arr[i]
                if sum > right_sum:
                    right_sum = sum
                    max_right = i

            return (max_left, max_right, left_sum + right_sum)

        def max_subarray_recursive(arr: List[float], low: int, high: int) -> Tuple[int, int, float]:
            if low == high:
                return (low, high, arr[low])

            mid = (low + high) // 2
            left_low, left_high, left_sum = max_subarray_recursive(arr, low, mid)
            right_low, right_high, right_sum = max_subarray_recursive(arr, mid + 1, high)
            cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)

        return max_subarray_recursive(arr, 0, len(arr) - 1)

    def closest_pair(self, points: List[Tuple[datetime, float]]) -> Tuple[Tuple[datetime, float], Tuple[datetime, float], float]:
        """
        Divide-and-conquer implementation of the closest pair of points algorithm.
        Returns (point1, point2, distance).
        """
        def distance(p1: Tuple[datetime, float], p2: Tuple[datetime, float]) -> float:
            return abs(p1[1] - p2[1])

        def brute_force(points: List[Tuple[datetime, float]]) -> Tuple[Tuple[datetime, float], Tuple[datetime, float], float]:
            min_distance = float('inf')
            pair = None
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    dist = distance(points[i], points[j])
                    if dist < min_distance:
                        min_distance = dist
                        pair = (points[i], points[j])
            return (*pair, min_distance)

        def strip_closest(strip: List[Tuple[datetime, float]], d: float) -> Tuple[Tuple[datetime, float], Tuple[datetime, float], float]:
            min_distance = d
            pair = None
            strip.sort(key=lambda point: point[1])

            for i in range(len(strip)):
                j = i + 1
                while j < len(strip) and (strip[j][1] - strip[i][1]) < min_distance:
                    dist = distance(strip[i], strip[j])
                    if dist < min_distance:
                        min_distance = dist
                        pair = (strip[i], strip[j])
                    j += 1

            return (*pair, min_distance) if pair else (None, None, float('inf'))

        def closest_util(points: List[Tuple[datetime, float]]) -> Tuple[Tuple[datetime, float], Tuple[datetime, float], float]:
            n = len(points)
            if n <= 3:
                return brute_force(points)

            mid = n // 2
            mid_point = points[mid]
            left = points[:mid]
            right = points[mid:]

            left_pair = closest_util(left)
            right_pair = closest_util(right)

            if left_pair[2] < right_pair[2]:
                d = left_pair[2]
                min_pair = left_pair
            else:
                d = right_pair[2]
                min_pair = right_pair

            strip = [p for p in points if abs(p[1] - mid_point[1]) < d]
            strip_pair = strip_closest(strip, d)

            if strip_pair[2] < min_pair[2]:
                return strip_pair
            else:
                return min_pair

        points.sort(key=lambda x: x[1])
        return closest_util(points)

    def analyze(self) -> dict:
        """
        Perform the financial data analysis.
        """
        if not self.data:
            return {"error": "No data available for analysis"}

        # Step 1: Sort the data by closing price
        sorted_data = self.merge_sort(self.data)

        # Step 2: Find period of maximum gain
        price_changes = [b[1] - a[1] for a, b in zip(sorted_data[:-1], sorted_data[1:])]
        max_gain_period = self.max_subarray(price_changes)

        # Step 3: Detect anomalies
        anomalies = self.closest_pair(sorted_data)

        # Step 4: Generate report
        report = {
            "sorted_data": [(d.strftime("%Y-%m-%d"), price) for d, price in sorted_data[:-1]],  # Return all data
            "max_gain_period": {
                "start_index": max_gain_period[0],
                "end_index": max_gain_period[1],
                "max_gain": max_gain_period[2]
            },
            "anomalies": {
                "point1": (anomalies[0][0].strftime("%Y-%m-%d"), anomalies[0][1]),
                "point2": (anomalies[1][0].strftime("%Y-%m-%d"), anomalies[1][1]),
                "distance": anomalies[2]
            }
        }

        return report

if __name__ == "__main__":
    file_path = "a.us.txt"  # Add file here
    try:
        fas = StockAnalysisSystem(file_path)
        analysis_report = fas.analyze()

        print("All entries of Sorted Data (by closing price):", analysis_report["sorted_data"])
        print("Max Gain Period:", analysis_report["max_gain_period"])
        print("Anomalies:", analysis_report["anomalies"])
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your input file and ensure it contains valid financial data.")
