import {useState} from 'react';

export default function SearchNasa(props){

    const [search , setSearch]=useState("");

    const handleSearch =(event)=>{
        setSearch(event.target.value);
    }

    const handleApod=()=>{
        props.getApod(search);

    }
    
    return(
        <div className="Search">
            <input type="text" onChange={handleSearch}/>
            <input type="button" value="Search" onClick={handleApod}/>
            
        </div>

        

    )

}