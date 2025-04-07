## 🗃️ Database Schema

### 📁 `appointments`
| Column            | Type        | Description                                   |
|-------------------|-------------|-----------------------------------------------|
| `id`              | UUID        | Primary key                                   |
| `user_id`         | UUID        | References user                               |
| `therapist_id`    | UUID        | References therapist                          |
| `scheduled_at`    | Timestamp   | Date and time of the session                  |
| `status`          | String      | Appointment status (e.g., scheduled, done)    |
| `package_type`    | String      | Type of package (single, monthly, intensive)  |
| `created_at`      | Timestamp   | Record creation time                          |
| `pre_session_message` | Text   | Optional message before session               |

---

### 📁 `entries`
| Column         | Type      | Description                       |
|----------------|-----------|-----------------------------------|
| `id`           | UUID      | Primary key                       |
| `user_id`      | UUID      | References user                   |
| `content`      | Text      | Entry text                        |
| `created_at`   | Timestamp | Creation timestamp                |
| `language_code`| String    | Language of the entry             |

---

### 📁 `login_attempts`
| Column         | Type      | Description                      |
|----------------|-----------|----------------------------------|
| `id`           | UUID      | Primary key                      |
| `user_id`      | UUID      | References user                  |
| `ip_address`   | String    | IP address of login attempt      |
| `success`      | Boolean   | Whether login was successful     |
| `attempted_at` | Timestamp | When the attempt was made        |

---

### 📁 `matches`
| Column         | Type      | Description                             |
|----------------|-----------|-----------------------------------------|
| `id`           | UUID      | Primary key                             |
| `entry_id`     | UUID      | References an entry                     |
| `therapist_id` | UUID      | References matched therapist            |
| `match_score`  | Float     | Matching score based on vector similarity |
| `rank`         | Integer   | Ranking of therapist for that entry     |
| `created_at`   | Timestamp | When the match was generated            |

---

### 📁 `notifications`
| Column         | Type      | Description                            |
|----------------|-----------|----------------------------------------|
| `id`           | UUID      | Primary key                            |
| `user_id`      | UUID      | References user                        |
| `message`      | Text      | Notification message                   |
| `is_read`      | Boolean   | Read/unread status                     |
| `type`         | String    | Type of notification                   |
| `created_at`   | Timestamp | When it was sent                       |

---

### 📁 `payments`
| Column               | Type      | Description                        |
|----------------------|-----------|------------------------------------|
| `id`                 | UUID      | Primary key                        |
| `user_id`            | UUID      | References user                    |
| `appointment_id`     | UUID      | References appointment             |
| `stripe_transaction_id` | String | Stripe payment reference           |
| `amount`             | Decimal   | Payment amount                     |
| `package_type`       | String    | Package paid for                   |
| `created_at`         | Timestamp | When the payment was made          |

---

### 📁 `session_recordings`
| Column         | Type      | Description                        |
|----------------|-----------|------------------------------------|
| `id`           | UUID      | Primary key                        |
| `appointment_id`| UUID     | References appointment             |
| `video_url`    | String    | Link to video recording            |
| `expires_at`   | Timestamp | When the video link expires        |
| `created_at`   | Timestamp | When the recording was saved       |

---

### 📁 `therapist_availability`
| Column         | Type      | Description                        |
|----------------|-----------|------------------------------------|
| `id`           | UUID      | Primary key                        |
| `therapist_id` | UUID      | References therapist               |
| `available_date`| Date     | Available day for booking          |
| `created_at`   | Timestamp | Record creation time               |

---

### 📁 `therapist_bios`
| Column         | Type      | Description                        |
|----------------|-----------|------------------------------------|
| `id`           | UUID      | Primary key                        |
| `therapist_id` | UUID      | References therapist               |
| `language_code`| String    | Language of the bio                |
| `bio`          | Text      | Therapist bio text                 |

---

### 📁 `therapists`
| Column              | Type      | Description                        |
|---------------------|-----------|------------------------------------|
| `id`                | UUID      | Primary key                        |
| `email`             | String    | Login email                        |
| `password_hash`     | String    | Hashed password                    |
| `full_name`         | String    | Therapist's full name              |
| `profile_picture_url` | String  | Link to profile picture            |
| `created_at`        | Timestamp | Registration date                  |
| `bio`               | Text      | Default bio                        |
| `language`          |
