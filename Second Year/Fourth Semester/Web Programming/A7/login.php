<?php 
  session_start();

  $mysqli = new mysqli('localhost', 'root', '', 'lab7');

  if ($_SESSION['logged_in'] == 'true') {
    header("location: index.php");
  } else {
    $_SESSION['message'] = '';
    $_SESSION['logged_in'] = 'false';
  }

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $username = $_POST['username'];
    $password = md5($_POST['password']);

    $sql = "SELECT * FROM User WHERE username='" . $username . "' AND password='" . $password . "' LIMIT 1";

    $response = mysqli_query($mysqli, $sql);

    if (mysqli_num_rows($response) == 1) {

      while($row = mysqli_fetch_array($response)){
        $_SESSION['user_id'] = ''. $row['id'] .'';
      }

      $_SESSION['message'] = 'Welcome, '. $username .'!';
      $_SESSION['logged_in'] = 'true';
      header("location: index.php");
    }

  }

?>  

<!DOCTYPE html>
<html>

<head>
  <title>News Service</title>
  <link rel="stylesheet" type="text/css" href="main.css">
  <script src="https://code.jquery.com/jquery-3.3.1.js"></script>

<script>
    $(document).ready(function() {
      $('.filter-by-category').click(function() {
        var filter_by_category = $('#category-filter').find(':selected').text();
        
        $('#news').load("category-filter.php", {
          selected_category: filter_by_category
        });
      });

      $('.filter-by-date').click(function() {
        var filter_by_date = $('#date-filter').find(':selected').text();
        
        $('#news').load("date-filter.php", {
          selected_date: filter_by_date
        });
      });

    });

    function setDateAsPrevious() {
      document.getElementById("previous-filter").innerHTML = "Previously used: Date filter";
    }

    function setCategoryAsPrevious() {
      document.getElementById("previous-filter").innerHTML = "Previously used: Category filter";
    }

  </script>
  </head>

<body>

  <div class="login-page">
    <div class="form">

      <? echo(md5('password')) ?>

      <form class="login-form" method="POST" action="login.php">

        <input type="text" placeholder="username" name="username" required/>
        <input type="password" placeholder="password" name="password" required/>

        <input class="submit" type="submit" name="login" value="Login">

        <p class="message">Are you not registered? <a href="register.php">Create an account</a></p>

      </form>

    </div>
  </div>
 

  <div id="previous-filter">
  
    </div>

  <center>

    

    <div id="main">

      <h1> News </h1>
      <div style="float: left;">

        <select id="category-filter">
        <?php 
          
          $sql = "SELECT DISTINCT category FROM News";
          $result = mysqli_query($mysqli, $sql);

          if (mysqli_num_rows($result) > 0) {
            while($row = mysqli_fetch_assoc($result)){
              $category = ''. $row['category'] .'';

              echo '<option>'. $category .'</option>';
            }
          }

        ?>
        </select>

        <button class="filter-by-category" onclick="setCategoryAsPrevious()"> Filter </button>

      </div> 

      <div style="float: right;">

        <select id="date-filter">

          <?php 
          
            $sql = "SELECT DISTINCT date FROM News";
            $result = mysqli_query($mysqli, $sql);

            if (mysqli_num_rows($result) > 0) {
              while($row = mysqli_fetch_assoc($result)){
                $date = ''. $row['date'] .'';

                echo '<option>'. $date .'</option>';
              }
            }

          ?>

        </select>

        <button class="filter-by-date" onclick="setDateAsPrevious()"> Filter </button>

      </div> 

      <br />
      <br />

      <div id="news">

        <?php
          
          $sql = "SELECT * FROM News ORDER BY date DESC";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $title = ''. $row['title'] .'';
            $description = ''. $row['content'] .'';
            $producer = ''. $row['producer'] .'';
            $category = ''. $row['category'] .'';
            $date = ''. $row['date'] .'';
            $user_id = ''. $row['user_id'] .'';

            echo '<div style="margin-bottom: 75px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $title .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $description .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $producer .', '. $category .', '. $date .'</h5>';
            if ($_SESSION['user_id'] == $user_id) {
              echo '<form method="POST" action="index.php">';
              echo '<button style="margin-bottom: 50px;" class="edit" type="submit" name="edit" value="'.$id.'"> Edit </button>';
              echo '</form>';
            }
            echo '</div>';
          }

        ?>

      </div>

    </div>
  </center>

</body>

</html>