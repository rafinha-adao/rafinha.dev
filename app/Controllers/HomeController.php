<?php

namespace App\Controllers;

class HomeController extends BaseController
{
    public function index(): string
    {
        if (ENVIRONMENT == 'production') {
            $this->cachePage(3600);
        }

        return view('pages/home');
    }
}
