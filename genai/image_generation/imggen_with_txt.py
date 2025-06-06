# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def generate_images(output_gcs_uri: str) -> str:
    # [START googlegenaisdk_imggen_with_txt]
    from google import genai
    from google.genai.types import GenerateImagesConfig

    client = genai.Client()

    # TODO(developer): Update and un-comment below line
    # output_gcs_uri = "gs://your-bucket/your-prefix"

    image = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt="A dog reading a newspaper",
        config=GenerateImagesConfig(
            aspect_ratio="1:1",
            number_of_images=1,
            safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
            person_generation="DONT_ADULT",
            output_gcs_uri=output_gcs_uri,
        ),
    )

    # Example response:
    # gs://your-bucket/your-prefix
    print(image.generated_images[0].image.gcs_uri)
    # [END googlegenaisdk_imggen_with_txt]
    return image.generated_images[0].image.gcs_uri


if __name__ == "__main__":
    generate_images(output_gcs_uri="gs://your-bucket/your-prefix")
