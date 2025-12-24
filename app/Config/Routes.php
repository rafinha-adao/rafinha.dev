<?php

use App\Controllers\HomeController;
use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
$routes->get('/', [HomeController::class, 'index']);

$routes->get('/noshorts', function() {
    return view('pages/noshorts');
});
