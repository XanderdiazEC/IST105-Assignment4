<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment Form</title>
</head>
<body>
    <h1>Enter Numerical Values</h1>
    <form action="process.php" method="post">
        <label for="a">Value for a:</label>
        <input type="number" id="a" name="a" required><br><br>

        <label for="b">Value for b:</label>
        <input type="number" id="b" name="b" required><br><br>

        <label for="c">Value for c:</label>
        <input type="number" id="c" name="c" required><br><br>

        <input type="submit" value="Calculate">
    </form>
</body>
</html>