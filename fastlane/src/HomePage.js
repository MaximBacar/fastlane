import React, { useState } from 'react';
import CompactCarImg from './Images/CompactCarImg.png';
import MediumCarImg from './Images/MediumCarImg.png';
import FullSizeImg from './Images/FullSizeImg.png';
import Class1TruckImg from './Images/Class1TruckImg.png';
import Class2TruckImg from './Images/Class2TruckImg.png';

const HomePage = () => {
  const [selectedVehicle, setSelectedVehicle] = useState(null);

  const squareStyle = {
    width: '182px',
    height: '182px',
    backgroundColor: 'white',
    margin: '20px',
    borderRadius: '25px',
    border: `1px solid ${selectedVehicle ? (selectedVehicle === 'CompactCar' ? '#0583D2' : 'black') : 'black'}`,
    alignItems: 'center',
    display: 'flex',
    justifyContent: 'center',
    cursor: 'pointer',
  };

  const titleStyle = {
    fontFamily: 'Nunito',
    fontSize: '34px',
    fontStyle: 'italic',
    fontWeight: 'bold',
    backgroundColor: '#0583D2',
    padding: '20px',
    display: 'flex',
  };

  const subtitleStyle = {
    fontSize: '24px',
    textAlign: 'center',
    marginTop: '10px',
  };

  const buttonStyle = {
    width: '162px',
    height: '52px',
    backgroundColor: 'black',
    borderRadius: '25px',
    color: 'white',
    fontSize: '18px',
    fontWeight: 'bold',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    cursor: 'pointer',
  };

  const handleVehicleClick = (vehicleType) => {
    setSelectedVehicle(vehicleType);
    // Add any additional logic or actions when a vehicle is clicked
  };

  return (
    <div style={{ flexDirection: 'column' }}>
      <div style={titleStyle}>FastLane</div>

      <div style={subtitleStyle}>Select your vehicle type</div>

      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', borderRadius: '25px' }}>
        <div style={{ ...squareStyle, border: `2px solid ${selectedVehicle ? (selectedVehicle === 'CompactCar' ? '#0583D2' : 'black') : 'black'}` }} onClick={() => handleVehicleClick('CompactCar')}>
          <img src={CompactCarImg} alt="Compact Car" style={{ width: '78px', height: '78px', marginBottom: '10px' }} />
        </div>

        <div style={{ ...squareStyle, border: `2px solid ${selectedVehicle ? (selectedVehicle === 'MediumCar' ? '#0583D2' : 'black') : 'black'}` }} onClick={() => handleVehicleClick('MediumCar')}>
          <img src={MediumCarImg} alt="Medium Car" style={{ width: '115px', height: '115px', marginBottom: '10px' }} />
        </div>

        <div style={{ ...squareStyle, border: `2px solid ${selectedVehicle ? (selectedVehicle === 'FullSizeCar' ? '#0583D2' : 'black') : 'black'}` }} onClick={() => handleVehicleClick('FullSizeCar')}>
          <img src={FullSizeImg} alt="Full-Size Car" style={{ width: '115px', height: '115px', marginBottom: '10px' }} />
        </div>
      </div>

      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ ...squareStyle, border: `2px solid ${selectedVehicle ? (selectedVehicle === 'Class1Truck' ? '#0583D2' : 'black') : 'black'}` }} onClick={() => handleVehicleClick('Class1Truck')}>
          <img src={Class1TruckImg} alt="Class1 Truck" style={{ width: '115px', height: '115px', marginBottom: '10px' }} />
        </div>

        <div style={{ ...squareStyle, border: `2px solid ${selectedVehicle ? (selectedVehicle === 'Class2Truck' ? '#0583D2' : 'black') : 'black'}` }} onClick={() => handleVehicleClick('Class2Truck')}>
          <img src={Class2TruckImg} alt="Class2 Truck" style={{ width: '115px', height: '115px', marginBottom: '10px' }} />
        </div>
      </div>

      <div style={{ position: 'absolute', bottom: '50px', right: '75px' }}>
        <div style={buttonStyle}>Book</div>
      </div>
    </div>
  );
};

export default HomePage;
