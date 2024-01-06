package com.example.animateapp

import android.app.Application
import com.example.animateapp.data.AppContainer
import com.example.animateapp.data.AppDataContainer

class AnimateApplication : Application() {

    lateinit var container: AppContainer

    override fun onCreate() {
        super.onCreate()
        container = AppDataContainer(this)
    }
}