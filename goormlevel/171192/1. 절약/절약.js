// Run by Node.js
const readline = require('readline');
let N = null;
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let money = 0;
	for await (const line of rl) {
		if (!N){
			N=line;
		} else{
			const [a, b] = line.split(' ');
			if (a=='in'){
				money+=Number(b);
			} else{
				money -= Number(b);
			}
			if (money<0){
				console.log('fail');
				process.exit();
			}
		}
	}
	console.log('success');
	process.exit();
})();
