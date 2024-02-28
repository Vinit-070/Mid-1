// Middleware Example in Node js using Connect

var connect = require('connect');
var app = connect();
// respond to all requests
app.use(function f1(req, res, next){
    console.log("Middleware 1")
    next();

  })
app.use(function f2(req, res, next){
    console.log("Middleware 2")
    next();

  })
  app.listen(3000);
  

/*
  // Middleware syntax in pure node js using connect

  app.use(function f1(req, res, next){
    // Middleware 1
    next()
  });
  
  
  */
  
