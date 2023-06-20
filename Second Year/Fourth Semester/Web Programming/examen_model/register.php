<?php 
  session_start();

  if ($_SESSION['logged_in'] == 'true') {
    $_SESSION['login'] = 'Log out';
    header("location: index.php");
  } else {
    $_SESSION['message'] = '';
    $_SESSION['logged_in'] = 'false';
  }

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    
      $name = $_POST['name'];
      $age = $_POST['age'];
      $skills = $_POST['skills'];

      $_SESSION['name'] = $name;

      $sql = "INSERT INTO SoftwareDeveloper (name, age, skills) VALUES ('$name', '$age', '$skills') ";

      if ($mysqli->query($sql) === true) {
        
        $get_user = "SELECT * FROM SoftwareDeveloper WHERE name='" . $name . "'";

        $response = mysqli_query($mysqli, $get_user);

        while($row = mysqli_fetch_array($response)){
          $_SESSION['user_id'] = ''. $row['id'] .'';
        }

        $_SESSION['message'] = 'Welcome, '. $name .'!';
        $_SESSION['logged_in'] = 'true';
        $_SESSION['selected_project_id'] = '';
        header("location: index.php");
      } else {
        $_SESSION['message'] = 'User could not be saved to the database!';
      }

  }

?>

<!DOCTYPE html>
<html>

<head>
  <title>Projects</title>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>

  <div class="login-page">
    <div class="form">

      <form class="register-form" method="POST" action="register.php">

        <div style="margin-bottom: 15px;">
          <?= $_SESSION['message'] ?>
        </div>

        <input type="text" placeholder="name" name="name" required/>
        <input type="text" placeholder="age" name="age" required/>
        <input type="text" placeholder="skills" name="skills" required/>
        
        <input class="submit" type="submit" name="register" value="Register">

        <p class="message">Already registered? <a href="login.php">Sign In</a></p>

      </form>

    </div>
  </div>

</body>

</html>