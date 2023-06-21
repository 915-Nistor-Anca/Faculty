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
        header("location: filterbycity.php");
        exit;
      }
  }
?>

<!DOCTYPE html>
<html>

<head>
  <title>Cities</title>
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
      <input class="form" type="text" name="filter" placeholder="City name:">
      <input class="submit" type="submit" name="search" value="Search">
    </form>
  </div>

    

<center>
    <div id="main">

      <h1> Cities </h1>

        <?php
          
          $sql = "SELECT * FROM city";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $name = ''. $row['name'] .'';
            $county = ''. $row['county'] .'';

            echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $id .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $name .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $county .'</h5>';

            //echo '<form method="POST" action="filterbycity.php">';
            //echo '<button style="margin-bottom: 50px;" class="submit" type="submit" name="filter" value="' . $name . '">Search</button>';
            //echo '</form>';

            echo '</div>';
          }

        ?>
      </div>


      <div id="main">

      <h1> Cities ordered by metric </h1>

        <?php
          
          $sql = "SELECT *,((0.6 * l.duration) + (0.4 * l.distance)) as metric  FROM city c JOIN link l ON c.id = l.idcity1 OR c.id = l.idcity2 ORDER BY ((0.6 * l.duration) + (0.4 * l.distance))";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $name = ''. $row['name'] .'';
            $county = ''. $row['county'] .'';
            $metric = ''. $row['metric'] .'';
          

            echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $id .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $name .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $county .', '. $metric .'</h5>';
            
            echo '</div>';
        }
        ?>
      </div>
  </center>
</body>

</html>
      
