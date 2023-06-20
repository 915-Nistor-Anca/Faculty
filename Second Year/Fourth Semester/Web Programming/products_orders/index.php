<?php
session_start();
$mysqli = new mysqli('localhost', 'root', '', 'examen_model');

if ($_SESSION['logged_in'] == 'false') 
  {
    $_SESSION['login'] = 'Log in';
    $_SESSION['user_id'] = '';
    header("location: login.php");
  } 
  else 
  {
    $_SESSION['login'] = 'Log out';
  }

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    if (isset($_POST['logout'])) {

      if ($_SESSION['logged_in'] == 'true') {
        $_SESSION['logged_in'] = 'false';
        $_SESSION['message'] = '';
        
        header("location: index.php");
        exit;
      } else {
        header("location: login.php");
        exit;
      }
    }

    if (isset($_POST['add'])) {
      header("location: add.php");
      exit;
    }

      if (isset($_POST['filter'])) {
        $_SESSION['filtered_name'] = $_POST['filter'];
        header("location: filterbystring.php");
        exit;
      }
  }
?>

<!DOCTYPE html>
<html>

<head>
  <title>Products</title>
  <link rel="stylesheet" type="text/css" href="main.css">
  <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
</head>

<body>

  <div style="float: right;">
    <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="index.php">
      <input class="submit" type="submit" name="logout" value="<?= $_SESSION['login']?>">
    </form>
  </div>

  
  <div style="float: left;">
    <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="">
      <input class="form" type="text" name="filter" placeholder="Product name:">
      <input class="submit" type="submit" name="search" value="Search">
    </form>
  </div>

  <div style="float: right;">
  <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="">
  <input class="submit" type="submit" name="add" value="Add product">
  </form>
  </div>
    

<center>
    <div id="main">

      <h1> Products </h1>

        <?php
          
          $sql = "SELECT * FROM products";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $name = ''. $row['name'] .'';
            $description = ''. $row['description'] .'';

            echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $name .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $id .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $description .'</h5>';
            
            echo '</div>';
          }

        ?>
      </div>
  </center>
</body>

</html>
      
