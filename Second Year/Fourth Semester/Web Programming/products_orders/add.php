<?php 
  session_start();

  if ($_SESSION['logged_in'] == 'false') {
    $_SESSION['login'] = 'Log in';
    $_SESSION['message'] = '';
    header("location: index.php");
  }

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $name = $_POST['name'];
    $description = $_POST['description'];

    $sql = "INSERT INTO products (name, description) " . "VALUES ('$name', '$description')";
    if ($mysqli->query($sql) === true) {
        header("location: index.php");
      } else {
        $_SESSION['message'] = 'The product could not be saved to the database!';
      }
    }
?>

<!DOCTYPE html>
<html>

<head>
  <title>Products</title>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>

  <div class="login-page">
    <div class="form">

      <form class="register-form" method="POST" action="add.php">

        <div style="margin-bottom: 15px;">
          <?= $_SESSION['message'] ?>
        </div>

        <input type="text" placeholder="name" name="name" required/>
        <input type="text" placeholder="description" name="description" required/>

        <input class="submit" type="submit" name="create" value="Add product">

      </form>

    </div>
  </div>

</body>

</html>