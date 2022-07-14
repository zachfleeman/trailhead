import axios from 'axios'
import { apiHost } from '@/env'

export const api = {
    async getRecords(start_date, end_date) {
        return axios.post(`${apiHost}/api/records/`, {from_date: start_date, to_date: end_date});
    },
    async login(accessKey, secretKey, region) {
        return axios.post(`${apiHost}/api/credentials`, {access_key: accessKey, secret_key: secretKey, region: region});
    }

}