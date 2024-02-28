// Create simple http server in node js
var http = require('http');
http.createServer(function(req, res){
res.write('Hello World!');
res.end();
}).listen(3000);



/*const http = require('http');

// Create an HTTP server
const server = http.createServer((req, res) => {
  // Set the response HTTP status code and content type
  res.writeHead(200, {'Content-Type': 'text/plain'});
  
  // Send the response body
  res.end('Hello World\n');
});

// Listen on port 3000
server.listen(3000, 'localhost', () => {
    console.log('Server running at http://localhost:3000/');
  });
  */
