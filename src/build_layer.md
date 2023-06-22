
# Steps to Build a Lambda Layer with Python Dependencies

1. Pull the latest version of the AWS SAM Build Image for Python 3.10

    ```bash
    docker pull public.ecr.aws/sam/build-python3.10:1.84.0-20230517004040
    ```

2. Run the container with the following command:

    ```bash
    docker run -it -v $(pwd):/var/task public.ecr.aws/sam/build-python3.10:1.84.0-20230517004040
    ```

3. Install all the dependencies in the requirements.txt file

    ```bash
    pip install -r requirements.txt -t python
    ```

4. Zip the contents of the python directory

    ```bash
    zip -r python.zip ./python
    ```

5. Create a new layer in the AWS Console and upload the zip file. Make sure to select Python 3.10 as the runtime. Guide to create a new layer can be found [here](https://medium.com/the-cloud-architect/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d).
