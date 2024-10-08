import { useEffect, useState } from 'react'; //1 

function ItemsList() {  //2 
    const [items, setItems] = useState([]); //3
 
    useEffect(() => { //4 
        fetch('http://localhost:3000/DEMOOO') //5 
            .then(response => response.json()) //6 
            .then(data => console.log(data)); //7 
    }, []); //8 

    return (
        <ul>
            {items.map((item, index) => (    //9 
                <li key={index}>{item}</li>  //10 
            ))}
        </ul>
    );
}
export default ItemsList; //11