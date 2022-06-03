import axios from 'axios';

export const api = {
    async getLogs() {
        return axios.get('http://127.0.0.1:8000/api/logs/?from_s=one%20hour%20ago&to_s=now');
    }
}