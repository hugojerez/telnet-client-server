'use strict'
 
const Telnet = require('telnet-client')
 
async function run() {
  let connection = new Telnet()
 
  // these parameters are just examples and most probably won't work for your use-case.
  let params = {
    host: '127.0.0.1',
    port: 23,
      shellPrompt: '/ # ', // or negotiationMandatory: false
      negotiationMandatory: false,
    timeout: 1500
  }
 
  try {
    await connection.connect(params)
  } catch (error) {
      console.error("👀")
    // handle the throw (timeout)
      throw new Error(error)
  }
 
  setInterval(async () => {
    
    let res = await connection.send('data').catch(a=>console.error(a))
    console.log('Testing result... 🙊 :', res)
  },1000)
}
 
run()