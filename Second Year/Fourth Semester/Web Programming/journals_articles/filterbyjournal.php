<?php
    session_start(); 
    
    $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

    $username = $_SESSION['username'];
    $filtered_name = $_SESSION['filtered_name'];
    echo $username;
    $sql = "SELECT * FROM articles WHERE user = '$username' and journalid = (select id from journals where name = '$filtered_name')";
    $response = mysqli_query($mysqli, $sql);
    

?>


<!DOCTYPE html>
<html>
    <body>
    <center>
        <div id="main">
            <h1> User's articles from a journal </h1>
            <?php
                if (mysqli_num_rows($response) > 0) {

                    while($row = mysqli_fetch_array($response)){
                        $id = ''. $row['id'] .'';
                        $user = ''. $row['user'] .'';
                        $journalid = ''. $row['journalid'] .'';
                        $summary = ''. $row['summary'] .'';
                        $date = ''. $row['date'] .'';
            
                        echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
                        echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $id .'</h2></b>';
                        echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $summary .'</h4>';
                        echo '<h5 style="margin-left: 20px; text-align: left;">'. $user .', '. $journalid .', '.$date.'</h5>';
                        
                        echo '</div>';
                        
                    }
            
                } else {
                    echo "No articles.";
                }
            ?>
        </div>
    </center>
    </body>
</html>