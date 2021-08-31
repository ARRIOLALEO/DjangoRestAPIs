import './App.css';
import {useState} from 'react'
function App() {
  const [TODOS,setTodos] = useState([])
  const axios = require('axios').default 
  const getAllTodos = async() =>{
    const reqst = await axios.get('http://127.0.0.1:8000/api/?format=json')
    setTodos(reqst.data)
  }
 getAllTodos()
  return (
    <div className="App">
      <header className="App-header">
        {TODOS.map(todo=>(
          <div key={todo.id}>
            <h1>{todo.title}</h1>
            <p>{todo.description}</p>
            </div>
        ))}
      </header>
    </div>
  );
}

export default App;
