const axios = require('axios');
module.exports = {
  Users: class {
    static all() {
      return axios.get('/users.json').then(resp => resp.data);
    }
  }
};
