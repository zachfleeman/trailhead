import { defineStore } from 'pinia'
import { api } from '@/api'
import router from '@/router';

export const useStore = defineStore('trailhead', {
 state: () => ({
    isLoggedIn: false,
    userIdentity: {},
    records: {}
 }),

 actions: {
    logout() {
        process.env.AWS_ACCESS_KEY_ID = null
        process.env.AWS_SECRET_ACCESS_KEY = null
        process.env.AWS_SESSION_TOKEN = null
        process.env.AWS_TOKEN_EXPIRATION = null
        process.env.AWS_DEFAULT_REGION = null
        this.$patch({
            userIdentity: null,
            isLoggedIn: false
        })

        if (router.currentRoute.value.path != '/login') {
            router.push('/login');
        }
    },
    async login(accessKey, secretKey, region) {
        const res = await api.login(accessKey, secretKey, region)
        if(res.status == 200){
            const userData = {
                user_id: res.data.UserId,
                account: res.data.Account,
                arn: res.data.Arn
            }
            this.$patch({
                userIdentity: userData,
                isLoggedIn: true
            })
            
            if (router.currentRoute.value.path === '/login') {
                router.push('/');
            }
        }
    },
    async getRecords() {
        const res = await api.getRecords()
        this.$patch({
            records: res.data.records
        })
    }
 },
 persist: true
})