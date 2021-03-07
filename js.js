function minPathSum(matrix) {
	// write code here
	let dp = [];
	for (let i = 0; i < matrix.length + 1; i++) {
		dp.push(Array(matrix[0].length + 1).fill(Infinity));
	}
	dp[0][1] = 0;
	for (let i = 1; i < dp.length; i++) {
		for (let j = 1; j < dp[0].length; j++) {
			dp[i][j] =
				Math.min(dp[i - 1][j], dp[i][j - 1]) + matrix[i - 1][j - 1];
		}
	}
	return dp.pop().pop();
}
module.exports = {
	minPathSum: minPathSum,
};
