// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = null;
	for await (const line of rl) {
		if (!line){
			rl.close();
		}
		if (!N){
			N = +line;
		}
		for (let i=0; i<N; i++){
			let s = "";
			for (let j=1; j<=N; j++){
				s += `${i*N+j} `;
			}
			console.log(s.trim());
		}
		rl.close();
	}
	
	process.exit();
})();
