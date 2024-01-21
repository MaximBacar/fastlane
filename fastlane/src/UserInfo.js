import React, { useState } from 'react';
import './UserInfo.css';
import UserInfoImg from './Images/UserInfoImg.webp';
import { Link } from 'react-router-dom';

const UserInfo = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    phoneNumber: '',
    email: '',
    vehicleRegistrationPlate: '',
  });

  const [phoneNumberError, setPhoneNumberError] = useState('');
  const [emailError, setEmailError] = useState('');
  const [registrationPlateError, setRegistrationPlateError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });

    if (name === 'phoneNumber') {
      validatePhoneNumber(value);
    }

    if (name === 'email') {
      validateEmail(value);
    }

    if (name === 'vehicleRegistrationPlate') {
      validateRegistrationPlate(value);
    }
  };

  const validatePhoneNumber = (phoneNumber) => {
    const phoneNumberRegex = /^\d{10}$/;
    if (!phoneNumberRegex.test(phoneNumber)) {
      setPhoneNumberError('Phone number must contain 10 digits.');
    } else {
      setPhoneNumberError('');
    }
  };

  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setEmailError('Please enter a valid email address.');
    } else {
      setEmailError('');
    }
  };

  const validateRegistrationPlate = (registrationPlate) => {
    const registrationPlateRegex = /^[A-Za-z0-9]{5,7}$/;
    if (!registrationPlateRegex.test(registrationPlate)) {
      setRegistrationPlateError('Must contain 5 to 7 alphanumeric characters.');
    } else {
      setRegistrationPlateError('');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (phoneNumberError || emailError || registrationPlateError) {
      alert('Please fix the form errors before submitting.');
      return;
    }

    // Continue with form submission logic
    console.log('Form data submitted:', formData);
  };

  return (
    <div className='page-content' style={{ margin: 150, display: 'flex' }}>
      <div style={{ flex: 1, marginRight: 50 }}>
        <h1>User Information</h1>

        <div className='user-details'>
          <form onSubmit={handleSubmit}>
            <div>
              <label htmlFor='firstName'>First Name</label>
              <input
                type='text'
                id='firstName'
                name='firstName'
                value={formData.firstName}
                onChange={handleChange}
                required
              />
            </div>

            <div>
              <label htmlFor='lastName'>Last Name</label>
              <input
                type='text'
                id='lastName'
                name='lastName'
                value={formData.lastName}
                onChange={handleChange}
                required
              />
            </div>

            <div>
              <label htmlFor='email'>Email {emailError && <span className='error'>{emailError}</span>}</label>
              <input
                type='email'
                id='email'
                name='email'
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div>
              <label htmlFor='phoneNumber'>Phone Number{phoneNumberError && <span className='error'>{phoneNumberError}</span>}</label>
              <input
                type='tel'
                id='phoneNumber'
                name='phoneNumber'
                value={formData.phoneNumber}
                onChange={handleChange}
                required
              />
            </div>

            <div>
              <label htmlFor='vehicleRegistrationPlate'>Vehicle Registration Plate{registrationPlateError && <span className='error'>{registrationPlateError}</span>}</label>
              <input
                type='text'
                id='vehicleRegistrationPlate'
                name='vehicleRegistrationPlate'
                value={formData.vehicleRegistrationPlate}
                onChange={handleChange}
                required
              />
            </div>
            <Link to="/Calendar">
            <button type='submit'>Submit</button>
            </Link>
          </form>
        </div>
      </div>

      <div className='UserInfoImg'>
        <img src={UserInfoImg} alt='UserInfoImg' style={{ width: '100%', height: 'auto', marginRight:'200px' }} />
      </div>
    </div>
  );
};

export default UserInfo;
