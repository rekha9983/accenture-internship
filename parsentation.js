var presentation = ["html" ,"css" , "js" , "react" , "angular" , "bootstrap" ];

var business = ["nodejs"  , "java" , "dotnet", "python" ];

var data = ["mongodb", "sql" , "oracle", "cassandra" ];

//use the spread operator to represent the full stack 

var fullstack = [...presentation  , ...business , ...data ]

var fullstack2 = [presentation + business + data];

console.log(fullstack);

console.log(fullstack2);


