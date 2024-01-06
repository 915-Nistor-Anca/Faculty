package com.example.animateapp.ui

import androidx.lifecycle.ViewModelProvider.AndroidViewModelFactory
import androidx.lifecycle.createSavedStateHandle
import androidx.lifecycle.viewmodel.CreationExtras
import androidx.lifecycle.viewmodel.initializer
import androidx.lifecycle.viewmodel.viewModelFactory
import com.example.animateapp.AnimateApplication
import com.example.animateapp.ui.home.HomeViewModel
import com.example.animateapp.ui.movie.MovieDetailsViewModel
import com.example.animateapp.ui.movie.MovieEditViewModel
import com.example.animateapp.ui.movie.MovieEntryViewModel

object AppViewModelProvider {
    val Factory = viewModelFactory {
        initializer {
            MovieEditViewModel(
                this.createSavedStateHandle(),
                animateappApplication().container.moviesRepository
            )
        }
        initializer {
            MovieEntryViewModel(animateappApplication().container.moviesRepository)
        }

        initializer {
            MovieDetailsViewModel(
                this.createSavedStateHandle(),
                animateappApplication().container.moviesRepository
            )
        }

        initializer {
            HomeViewModel(animateappApplication().container.moviesRepository)
        }
    }
}

fun CreationExtras.animateappApplication(): AnimateApplication =
    (this[AndroidViewModelFactory.APPLICATION_KEY] as AnimateApplication)