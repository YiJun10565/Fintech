var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json());

//mysql
var mysql = require('mysql');
var con = mysql.createConnection({
    host    : 'localhost',
    user    : 'root',
    password: 'Song0815',
    database: 'fintech'
});


con.connect();

var data = {};
con.query('SELECT * from data', function (error, rows, fields) {
  if (error) throw error;
  data = rows;
});

//ejs
app.get('/', function(req, res){
    res.render('index.ejs', {data: data});
    console.log("running index.ejs");
});
app.get('/', function(req, res){
    res.render('index.ejs', {data: data});
    console.log("running index.ejs");
});
app.post('/input', function(req, res){
	var suspect = req.body.content;
	console.log(suspect);
	res.render('fintech.ejs', { Name : suspect,
	data: data
	})
});

//listen
app.listen(7680);
console.log('listening at 7680');
