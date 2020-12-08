function func1(){

    document.getElementById('print1').innerHTML = "";
    
    var rd1 = document.getElementById("male_radio");
    var rd2 = document.getElementById("female_radio");

    if(rd1.checked==true){

        link = 'https://first-serverless.vercel.app/api/index?gender=male'
        gender_type = "male"

        fetchData(link, gender_type)
    }     
    else if (rd2.checked==true){

        link = 'https://first-serverless.vercel.app/api/index?gender=female'
        gender_type = "female"
        
        fetchData(link, gender_type)
    }
    else{
        alert("Chose gender")
    }
} 


function fetchData(genderLink, gender) {

         fetch(genderLink)

        .then(response => {

            //console.log(response1)

            if (!response.ok){
                throw Error("ERROR");
            }         
            return response.json();
        })

        .then(input => {

            if (gender=="male"){    
            document.querySelector("#print1").insertAdjacentHTML("afterbegin",`<p> Name : ${input.male} </p>`);
            }

            else if (gender=="female"){
                document.querySelector("#print1").insertAdjacentHTML("afterbegin",`<p> Name : ${input.female} </p>`);
            }
        })

        .catch(error => {
            console.log(error);
        });
}
























