<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Student Registration Form</h1>
    <form>
        <label for="username">User Name: &nbsp; &nbsp;</label>
    <input type="text" name="name" id="name" placeholder="User Name">
    <br><br>
    <label for=""mail di> Mail id : &nbsp; &nbsp;</label>
    <input type="email" name="emaid" id="emaid" placeholder="Enter your email ID">
    <br><br>
    <label for="phone">Mobile number: &nbsp; &nbsp;</label>
    <input type="tel" name="number" id="number" placeholder="Please enter your number">
    <br><br>
    <label for="date">Date: &nbsp; &nbsp</label>
    <input type="date" name="date" id="date">
    <label for="gender">Gender: &nbsp;</label>
    <input type="radio" name="gender" id="gender">
    <label for="male">Male</label>
    <input type="radio" name="gender" id="gender">
    <label for="Female">Female</label>
    <input type="radio" name="gender" id="gender">
    <label for="Others">Others</label>
    <br><br>
    <label for="Skills">Skills: &nbsp; &nbsp;</label>
    <input type="checkbox" name="Python" id="python">
    <label for="Python">Python &nbsp;</label>
    <input type="checkbox" name="Java" id="Java">
    <label for="Java">Java &nbsp;</label>
    <input type="checkbox" name="C" id="C">
    <label for="C">C &nbsp;</label>
    <input type="checkbox" name="HTML" id="HTML">
    <label for="HTML">HTML &nbsp;</label>
    <br><br>
    <label for="Department">Department</label>
    <select name="Department" id="Department">
        <option value="select">--select course--</option>
        <option value="CSE">CSE</option>
        <option value="ECE">ECE</option>
        <option value="EEE">EEE</option>
    </select>
    <br><br>
    <label for="Year of Study">Year of study</label>
     <select name="year" id="year">
        <option value="select">--select course--</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
    </select>
    <label for="fileupload">Profile photo: &nbsp;</label>
    <input type="file" name="fileupload" id="fileupload">
    <br><br>
    <label for="fileupload">Resume: &nbsp;</label>
    <input type="file" name="fileupload" id="fileupload">
    <br><br>
    <label for="fileupload">Certificate: &nbsp;</label>
    <input type="file" name="fileupload" id="fileupload">
    <br><br>
    <h2>Education</h2>
    <table border="2">
        <th rowspan="1">S.no</th>
        <th rowspan="1">School/College</th>
        <th rowspan="1">Qualification</th>
        <th rowspan="1">Year</th>
        <th rowspan="1">Percentage</th>
        <tr>
            <td><input type="text" name="s.no" id="s.no" placeholder="s.no"></td>
            <td><input type="text" name="School/College" id="School/College" placeholder="School/College"></td>
            <td><input type="text" name="Qualification" id="Qualification" placeholder="Qualification"></td>
            <td><input type="text" name="Year" id="Year" placeholder="Year"></td>
            <td><input type="text" name="percentage" id="percentage" placeholder="%"></td>
        </tr>
        <tr>
            <td><input type="text" name="s.no" id="s.no" placeholder="s.no"></td>
            <td><input type="text" name="School/College" id="School/College" placeholder="School/College"></td>
            <td><input type="text" name="Qualification" id="Qualification" placeholder="Qualification"></td>
            <td><input type="text" name="Year" id="Year" placeholder="Year"></td>
            <td><input type="text" name="percentage" id="percentage" placeholder="%"></td>
        </tr>
        <tr>
            <td><input type="text" name="s.no" id="s.no" placeholder="s.no"></td>
            <td><input type="text" name="School/College" id="School/College" placeholder="School/College"></td>
            <td><input type="text" name="Qualification" id="Qualification" placeholder="Qualification"></td>
            <td><input type="text" name="Year" id="Year" placeholder="Year"></td>
            <td><input type="text" name="percentage" id="percentage" placeholder="%"></td>
        </tr>
        <tr>
            <td><input type="text" name="s.no" id="s.no" placeholder="s.no"></td>
            <td><input type="text" name="School/College" id="School/College" placeholder="School/College"></td>
            <td><input type="text" name="Qualification" id="Qualification" placeholder="Qualification"></td>
            <td><input type="text" name="Year" id="Year" placeholder="Year"></td>
            <td><input type="text" name="percentage" id="percentage" placeholder="%"></td>
        </tr>
    </table>
    <br><br>
    <label for="Address">Address: &nbsp;</label><br>
    <textarea name="Address" id="Address" rows="6" cols="60" placeholder="Enter your complete Address"></textarea>
    <br><br>
    <input type="checkbox">
    <label for="I agree the Terms and Conditions">I agree the Terms and Conditions</label>
    <br><br>
    <label for="button"></label>
    <button type="Register">Register</button>
    <button type="clear Form">Clear Form</button>
    </form>
</body>
</html>
