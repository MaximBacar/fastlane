import React, { useState, useEffect } from 'react';
import "./appointments.css"
function Appointments(){
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch('http://127.0.0.1:5000/getAppointments'); // Replace with your API endpoint
            const result = await response.json();
            setData(result);
          } catch (error) {
            console.error('Error fetching data:', error);
          }
        };
    
        fetchData();
      }, []);

    return(
        <div id='appointments'>
            <div id='content'>
              <h1 id='title'>Appointments</h1>
              <h2 id='day'>Today</h2>
              <div id="appointmentList">
                {data.map(item => (
                    <div key={item.id} className='appointment'>
                        <div id='titleBox'>
                          <div id='left'>
                            <h2 id='time' className='titles'>{item.start} - {item.end}</h2>
                            <h3 id='type' className='titles'>{item.type}</h3>
                          </div>
                          <div id='right'>
                            <h2 id='name' className='titles'>{item.full_name}</h2>
                            <h3 id='phone' className='titles'>{item.phone}</h3>
                          </div>
                        </div>

                        
                        {}
                    </div>
                ))}
              </div>
            
            </div>
        </div>
    )
}

export default Appointments;