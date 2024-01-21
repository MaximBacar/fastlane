import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import TimePicker from 'rc-time-picker';
import 'rc-time-picker/assets/index.css'; // Import the CSS for styling

const CustomCalendar = () => {
  
    
    
  const [date, setDate] = useState(new Date());

  // Set the min and max date to limit the calendar to October and November
  const minDate = new Date(date.getFullYear(), 9, 1); // October 1st
  const maxDate = new Date(date.getFullYear(), 10, 30); // November 30th

  const [selectedTime, setSelectedTime] = useState(); // State to store the selected time

  const handleTimeChange = (value) => {
    setSelectedTime(value);
  };

  const disabledHours = () => {
    // Disable hours before 7 AM and after 7 PM
    const hours = [];
    for (let i = 0; i < 24; i++) {
      if (i < 7 || i >= 19) {
        hours.push(i);
      }
    }
    return hours;
  };

  const disabledMinutes = (hour) => {
    // Disable minutes for the selected hour (e.g., 19:01 to 23:59)
    if (hour === 19) {
      const minutes = [];
      for (let i = 1; i < 60; i++) {
        minutes.push(i);
      }
      return minutes;
    }
    return [];
  };

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ marginRight: '20px', marginLeft: '50px' }}>
        <h2>Select Date</h2>
        <Calendar
          onChange={setDate}
          value={date}
          minDate={minDate}
          maxDate={maxDate}
          
        />

        <p className="selected-date">
          <span className='bold'>Selected Date:</span>{' '}
          {date.toDateString()}
        </p>
      </div>

      <div style={{ marginLeft: '200px', display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <h2>Select Time</h2>
        <TimePicker
          showSecond={false}
          defaultValue={selectedTime}
          onChange={handleTimeChange}
          format="h:mm a"
          disabledHours={disabledHours}
          disabledMinutes={disabledMinutes}
        />
        <p>
        Selected Time: {selectedTime ? selectedTime.format('h:mm a') : 'None'}
        </p>
      </div>
    </div>
  );
};

export default CustomCalendar;
