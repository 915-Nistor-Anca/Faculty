import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.example.animateapp.AddMovieScreen
import com.example.animateapp.AnimatedMovieList
import com.example.animateapp.AnimatedMovieViewModel
@Composable
fun AnimatedMoviesApp() {
    val viewModel: AnimatedMovieViewModel = viewModel()
    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = "list"
    ) {
        composable("list") {
            AnimatedMovieList(navController, viewModel)
        }
        composable("addMovie") {
            AddMovieScreen(navController, viewModel)
        }
        composable(
            "movieInformation/{movieId}",
            arguments = listOf(navArgument("movieId") { type = NavType.IntType })
        ) { backStackEntry ->
            val arguments = requireNotNull(backStackEntry.arguments)
            val movieId = arguments.getInt("movieId")
            val movie = viewModel.getAnimatedMovieById(movieId)
            if (movie != null) {
                AnimatedMovieInformationScreen(navController, movie, viewModel)
            } else {
                Text("Movie not found")
            }
        }

        composable(
            "updateMovie/{movieId}",
            arguments = listOf(navArgument("movieId") { type = NavType.IntType })
        ) { backStackEntry ->
            val arguments = requireNotNull(backStackEntry.arguments)
            val movieId = arguments.getInt("movieId")
            val movie = viewModel.getAnimatedMovieById(movieId)
            if (movie != null) {
                AnimatedMovieUpdateScreen(navController, viewModel, movie)
            } else {
                Text("Movie not found")
            }
        }

    }
}
