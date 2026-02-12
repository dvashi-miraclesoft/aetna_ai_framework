from locust import HttpUser, task, between

class AetnaMemberUser(HttpUser):
    # Simulate realistic human behavior: waiting 1 to 3 seconds between actions
    wait_time = between(1, 3)

    # The @task decorator tells Locust what actions the simulated user should take
    @task(1)
    def view_member_profile(self):
        """Simulates a user loading their profile dashboard."""
        self.client.get("/users/1", name="1. View Profile")

    @task(3) 
    def check_claims(self):
        """
        Simulates checking claims. 
        The @task(3) weight means this action is 3 times more likely to happen 
        than viewing the profile, simulating real-world heavy traffic areas.
        """
        self.client.get("/posts?userId=1", name="2. Check Claims")