package com.example.animateapp.ui.navigation

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.navArgument
import com.example.animateapp.ui.home.HomeDestination
import com.example.animateapp.ui.home.HomeScreen
import com.example.animateapp.ui.movie.MovieDetailsDestination
import com.example.animateapp.ui.movie.MovieDetailsScreen
import com.example.animateapp.ui.movie.MovieEditDestination
import com.example.animateapp.ui.movie.MovieEditScreen
import com.example.animateapp.ui.movie.MovieEntryDestination
import com.example.animateapp.ui.movie.MovieEntryScreen

@Composable
fun AnimateNavHost(
    navController: NavHostController,
    modifier: Modifier = Modifier,
) {
    NavHost(
        navController = navController,
        startDestination = HomeDestination.route,
        modifier = modifier
    ) {
        composable(route = HomeDestination.route) {
            HomeScreen(
                navigateToItemEntry = { navController.navigate(MovieEntryDestination.route) },
                navigateToItemUpdate = {
                    navController.navigate("${MovieDetailsDestination.route}/${it}")
                }
            )
        }
        composable(route = MovieEntryDestination.route) {
            MovieEntryScreen(
                navigateBack = { navController.popBackStack() },
                onNavigateUp = { navController.navigateUp() }
            )
        }
        composable(
            route = MovieDetailsDestination.routeWithArgs,
            arguments = listOf(navArgument(MovieDetailsDestination.movieIdArg) {
                type = NavType.IntType
            })
        ) {
            MovieDetailsScreen(
                navigateToEditItem = { navController.navigate("${MovieEditDestination.route}/$it") },
                navigateBack = { navController.navigateUp() }
            )
        }
        composable(
            route = MovieEditDestination.routeWithArgs,
            arguments = listOf(navArgument(MovieEditDestination.itemIdArg) {
                type = NavType.IntType
            })
        ) {
            MovieEditScreen(
                navigateBack = { navController.popBackStack() },
                onNavigateUp = { navController.navigateUp() }
            )
        }
    }
}