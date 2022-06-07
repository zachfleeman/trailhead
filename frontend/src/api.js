import axios from 'axios'
import { apiHost } from '@/env'

export const api = {
    async getRecords() {
        return axios.get(`${apiHost}/api/records/?from_s=one%20hour%20ago&to_s=now`);
    },
    async login(accessKey, secretKey) {
        return axios.post(`${apiHost}/api/credentials`, {accessKey, secretKey});
    }

}