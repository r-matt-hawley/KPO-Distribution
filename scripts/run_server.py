if __name__ == "__main__":
    import uvicorn
    uvicorn.run("kpo_dist_api.app:app", host="0.0.0.0", port=8000, reload=True)