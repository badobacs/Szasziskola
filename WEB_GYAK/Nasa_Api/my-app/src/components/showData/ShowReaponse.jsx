import NasaCards from "./NasaCards";

export default function ShowResponse(props){
    return(
        <div style={{
            display: 'flex',
            justifyContent: 'center',
            flexWrap: 'wrap'
        }}
        >
        {props.data.map(nasadata=> <NasaCards data={nasadata}/>)}    
        </div>
    )
}