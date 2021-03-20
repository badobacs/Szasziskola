import './App.css';
import {useState} from 'react';
import SearchNasa from './components/SearchNasa';
import ShowResponse from './components/showData/ShowReaponse';


function App() {

  const [data,setData] =useState([]);

  const fetchData = async(query)=>{
  const response = await fetch(`https://api.nasa.gov/planetary/${query}?api_key=nr6ZEH5EOfbhcQHtNoycjGH6PAyNCBhCXMy5yVQK`);
  const res= await response.json();
  console.log(res);
  if(res!=null){
    setData([res]);
  }
  setData([res]);
  }




  return (
    <div className="App">
      <SearchNasa getApod={fetchData}/>
      <ShowResponse data={data} />
    </div>
  );
}

export default App;
