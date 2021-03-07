function solve(a, b) {
	// write code here
	var new_mat = [];
	for (var i = 0; i < a.length; i++) {
		var new_row = [];
		for (var k = 0; k < b[0].length; k++) {
			var total = 0;
			for (var j = 0; j < b.length; j++) {
				total += a[i][j] * b[j][k];
			}
			new_row.push(total);
		}
		new_mat.push(new_row);
	}

	return new_mat;
}
module.exports = {
	solve: solve,
};

console.log(
	solve(
		[
			[1, 2],
			[3, 2],
		],
		[
			[3, 4],
			[2, 1],
		]
	)
);
