import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

const CustomCalendar = () => {
  const [date, setDate] = useState(new Date());

  // Set the min and max date to limit the calendar to October and November
  const minDate = new Date(date.getFullYear(), 9, 1); // October 1st
  const maxDate = new Date(date.getFullYear(), 10, 30); // November 30th

  return (
    <div>
      <h1>Calendar Example</h1>
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
  );
};

export default CustomCalendar;
