import React from 'react';
import {BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from '/Users/smatus/Documents/Python by example/project 1/_site2/static/containers/Layout.jsx';
import Login from '/Users/smatus/Documents/Python by example/project 1/_site2/static/containers/login.jsx';
import Home from '/Users/smatus/Documents/Python by example/project 1/_site2/static/pages/Home.jsx';
import NotFound from '/Users/smatus/Documents/Python by example/project 1/_site2/static/pages/NotFound.jsx';

const App = () => {
	return (
		<BrowserRouter>
			<Routes>
					<Route  path = "/" exact element = {<Home/>} />
					<Route  path = "/login" exact element = {<Login/>} />
					<Route exact element = {<NotFound/>} />
			</Routes>
		</BrowserRouter>

	);
}

export default App;
