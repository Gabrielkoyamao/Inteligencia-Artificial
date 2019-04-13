const express = require('express')
const app = express()
const PythonShell = require('python-shell');

app.get('/res/api', (req, res, next) => {


	res.send(JSON.stringify(req.query))
	// let options = {
	// 	mode: 'text',
	// 	pythonPath: 'C:\\Users\\gabri\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe',
	// 	scriptPath: '.\\',
	// 	args: [req.query.age, req.query.glycemie, req.query.shakiness, req.query.hunger, req.query.sweating, req.query.headach, req.query.diabetic_parents, req.query.pale, req.query.urination, req.query.thirst, req.query.blurred_vision, req.query.dry_mouth, req.query.smelling_breath, req.query.shortness_of_breath]
	// };

	// PythonShell.run('sistema_especialista.py', options, (err, results) => {
	// 	if (err) throw err;
	// 	// results is an array consisting of messages collected during execution
	// 	console.log(results);
	// 	res.json({
	// 		"res": results
	// 	})
	// });
});


app.get('/', (req, res) => {
	res.send('asdosadsad')
})

app.listen(8888, () => console.log('Example app listening on port 8888!'))