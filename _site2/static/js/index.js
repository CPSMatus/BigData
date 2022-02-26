/*
import React from 'react';
import ReactDom from 'react-dom';
import App from '/Users/smatus/Documents/Python by example/project 1/_site2/static/routes/app.jsx';

ReactDom.render(<App />, document.getElementById('app') );
*/

import React {useState} from 'react';

const Button = () => {
  const [name, setName] = useState('Hello World!');
    return (
      <div>
      <h1> {name}</h1>
      </div>
    );
}
