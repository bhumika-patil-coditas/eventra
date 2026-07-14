import { Controller, useForm } from "react-hook-form";
import { useLoginMutation, useRequestOTPMutation } from "../../redux/auth/authApi";
import { tokenStorage } from "../../utils/tokenStorage";
import { setAccessToken, setUser } from "../../redux/auth/authSlice";
import Form from "../../components/GenericComponents/Form/Form";
import Button from "../../components/GenericComponents/Button/Button";
import styles from "./LoginPanel.module.scss";
import FormInput from "../../components/GenericComponents/FormInput/FormInput";
import { useState } from "react";
import type { LoginData } from "./LoginPanel.types";
import { useDispatch } from "react-redux";

const LoginPanel = () => {

    const [login, { isLoading }] = useLoginMutation();
    const [requestOTP, { isLoading: isRequesting }] = useRequestOTPMutation();
    const [isLoginPanelOpen, setIsLoginPanelOpen] = useState(false);
    // const [getMe] = useLazyGetMeQuery();
    const dispatch = useDispatch();

    const { control, handleSubmit, formState: { errors } } = useForm({
        defaultValues: {
            email: "",
            otp: ""
        }
    });

    const onSubmit = async (data: LoginData) => {
        console.log("data", data)
        if (data.email && !data.otp) {
            try {
                const response = await requestOTP(data).unwrap();
                console.log(response)
                if (response) setIsLoginPanelOpen(true);
            } catch (error) {
                throw error;
            }

        } else {
            try {
                const payload = {
                    email: data.email,
                    code: data.otp
                }
                const response = await login(payload).unwrap();

                tokenStorage.setTokens(response.token);
                dispatch(setAccessToken(response.token));
                // const user = await getMe().unwrap();
                // dispatch(setUser(user));

            } catch (error) {
                throw error;
            }
        }
    }

    return (

        <div className={styles.loginPanel}>
            <div className={styles.leftSidePanel}>
                <img className={styles.logo} src="favicon.svg" alt="Logo" />
                <h1 >Welcome to Eventra</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>

            <div className={styles.formPanel}>
                <div className={styles.headingSection}>
                    <img className={styles.logo} src="logo.jpg" alt="" />
                </div>

                {!isLoginPanelOpen && <div className={styles.formDiv}>
                    <h2 className={styles.subHeading}>Login</h2>
                    <Form onSubmit={handleSubmit(onSubmit)}>
                        <Controller
                            name="email"
                            control={control}
                            rules={{
                                required: "Email is required"
                            }}
                            render={({ field }) => (
                                <FormInput
                                    {...field}
                                    placeholder="Enter your email"
                                />)}
                        />
                        {errors.email && <p>Email is required</p>}

                        <Button
                            type="submit"
                            className="primary"
                            disabled={isRequesting}
                            children={isRequesting ? "Requesting in..." : "Request OTP"}
                        />

                    </Form>
                </div>}

                {isLoginPanelOpen && <div className={styles.formDiv}>
                    <h2 className={styles.subHeading}>Enter OTP</h2>
                    <Form onSubmit={handleSubmit(onSubmit)}>
                        <Controller
                            name="otp"
                            control={control}
                            rules={{
                                required: "OTP is required"
                            }}
                            render={({ field }) => (
                                <FormInput
                                    {...field}
                                    placeholder="Enter OTP"
                                />)}
                        />
                        {errors.otp && <p>OTP is required</p>}

                        <Button
                            type="submit"
                            className="primary"
                            disabled={isLoading}
                            children={isLoading ? "Logging in..." : "Login"}
                        />

                    </Form>
                </div>
                }
            </div>
        </div>

    )
}

export default LoginPanel;