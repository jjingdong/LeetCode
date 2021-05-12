'''
Given an array of integers, determine the minimum cost to make it either
non-increasing or non-decreasing along its length. The cost to change an
element is the absolute difference between its initial value and its new value.
For example, if the element is initially 10, it can be changed to 7 for a
cost of 3.

Input: [0, 1, 2, 5, 6, 5, 7]
Output: 1

'''
# Solution online:

public static void main(String[] args) {
	int[] nums1 = { 0, 1, 2, 5, 6, 5, 7 };
	int[] nums2 = { 9847, 3752, 5621, 7012, 1986, 3090, 1383, 6257, 9501, 7004, 6181, 9387, 9137, 9305, 7795, 9310,
			3904, 8328, 6656, 8123, 1796, 2754, 4372, 5200, 3893, 8568, 4436, 3973, 8498, 1879, 2731, 4651, 4388,
			453, 2465, 2669, 6384, 819, 8565, 1952, 7219, 4362, 3012, 9380, 2645, 4800, 2945, 5778, 1993, 1170,
			1356, 8557, 1497, 8921, 670, 5155, 9115, 1095, 9400, 9451, 9344, 4393, 4201, 8167, 8129, 2004, 8839,
			1457, 7682, 1881, 9266, 6366, 9889, 242, 5318, 5248, 3670, 7381, 6567, 2317, 2162, 6670, 5876, 1179,
			2482, 9270, 4326, 4166, 6122, 2016, 3008, 5349, 1723, 5816, 4030 };
	System.out.println(getMinCost(nums1));
	System.out.println(getMinCost(nums2));
}

private static int getMinCost(int[] nums) {
	return Math.min(NoneDecreasingArray(nums, nums.length), NoneIncreasingArray(nums, nums.length));
}

public static int NoneDecreasingArray(int[] nums, int n) {
	int sum = 0, dif = 0;
	Queue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
	for (int i = 0; i < n; i++) {
		if (!maxHeap.isEmpty() && maxHeap.peek() >= nums[i]) {
			dif = maxHeap.peek() - nums[i];
			sum += dif;
			maxHeap.remove();
			maxHeap.add(nums[i]);
		}
		maxHeap.add(nums[i]);
	}

	return sum;
}

private static int NoneIncreasingArray(int[] nums, int n) {
	int sum = 0, dif = 0;
	Queue<Integer> minHeap = new PriorityQueue<>();
	for (int i = 0; i < n; i++) {
		if (!minHeap.isEmpty() && minHeap.peek() <= nums[i]) {
			dif = nums[i] - minHeap.element();
			sum += dif;
			minHeap.remove();
			minHeap.add(nums[i]);
		}
		minHeap.add(nums[i]);
	}
	return sum;
}

