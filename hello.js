process.stdin.setEncoding('utf8');
process.stdin.on('data',
    function (chunk) {
        process.stdout.write("Hello, World! \n" + chunk + "\n");
    });
process.stdin.on('end', function () {
    process.stdout.write("end");
})