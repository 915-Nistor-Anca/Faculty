<?php
    session_start(); 
    
    $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

    $filtered_name = $_SESSION['filtered_name'];
    $sql = "SELECT * FROM products WHERE name like '$filtered_name%'";
    $response = mysqli_query($mysqli, $sql);
    

?>


<!DOCTYPE html>
<html>
    <body>
    <center>
        <div id="main">
            <h1> Products starting with <?$filtered_name?> </h1>
            <?php
                if (mysqli_num_rows($response) > 0) {

                    while($row = mysqli_fetch_array($response)){
                        $id = ''. $row['id'] .'';
                        $name = ''. $row['name'] .'';
                        $description = ''. $row['description'] .'';
            
                        echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
                        echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $name .'</h2></b>';
                        echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $description .'</h4>';
                        echo '<h5 style="margin-left: 20px; text-align: left;">'. $id .'</h5>';
                        
                        echo '</div>';
                        
                    }
            
                } else {
                    echo "No products.";
                }
            ?>
        </div>
    </center>
    </body>
</html>