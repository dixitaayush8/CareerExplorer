import React, {useEffect} from 'react';
import './App.css';

function App() {
  const[keywords] = useState([]);

  useEffect(()=> {
    fetch('/getkeywordrecommendations').then(response => response.json().then(data => {
      setKeywords(data);
    }));
  }, []);

  return (
    <div className="App">

    </div>
  );
}

export default App;
